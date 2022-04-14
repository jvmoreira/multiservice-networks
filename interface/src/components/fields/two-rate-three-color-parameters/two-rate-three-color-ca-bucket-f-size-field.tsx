import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorCaBucketFSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorCaBucketFSize = useMemo(() => {
    return twoRateThreeColorParameters.ca_bucketF_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketFSize = useSetNfvTeFunctionParameter('ca_bucketF_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketFSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketFSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket C do Color Aware"
      name="ca-bucket-f-size"
      value={twoRateThreeColorCaBucketFSize}
      onChange={onTwoRateThreeColorBucketFSizeChangeHandler}
    />
  );
}
