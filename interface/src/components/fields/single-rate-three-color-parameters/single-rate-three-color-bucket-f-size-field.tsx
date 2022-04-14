import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorBucketFSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorBucketFSize = useMemo(() => {
    return singleRateThreeColorParameters.bucketF_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketFSize = useSetNfvTeFunctionParameter('bucketF_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketFSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketFSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket C"
      name="bucket-f-size"
      value={singleRateThreeColorBucketFSize}
      onChange={onSingleRateThreeColorBucketFSizeChangeHandler}
    />
  );
}
