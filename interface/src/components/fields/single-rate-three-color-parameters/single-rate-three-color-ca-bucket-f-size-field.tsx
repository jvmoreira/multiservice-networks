import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorCaBucketFSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorCaBucketFSize = useMemo(() => {
    return singleRateThreeColorParameters.ca_bucketF_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketFSize = useSetNfvTeFunctionParameter('ca_bucketF_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketFSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketFSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket C do Color Aware"
      name="ca-bucket-f-size"
      value={singleRateThreeColorCaBucketFSize}
      onChange={onSingleRateThreeColorBucketFSizeChangeHandler}
    />
  );
}
